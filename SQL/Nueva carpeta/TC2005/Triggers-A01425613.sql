use sistemaventas;

# Ejercicio 1
delimiter //
create trigger nuevoCliente
after insert on clientes
for each row
begin
    insert into auditoria(tablaAfectada, evento, descripcion, usuario, fecha)
    values('Clientes', 'INSERT', concat('Nuevo cliente registrado: ',
            NEW.nombre, ' Email: ', NEW.email),USER(), NOW());
end //
delimiter ;

select * from  clientes;
insert into clientes(nombre, email, fechaRegistro) values('Alex', 'aabf@gmail.com', now());
select * from auditoria;

# Ejercicio 2
delimiter //
create trigger validadPedido
before insert on pedidos
for each row
begin
    declare exist int default 0;
    select count(idCliente) into exist from clientes where clientes.idCliente = new.idCliente;
    if exist < 1 then
        signal sqlstate '45000'
        set message_text = 'El cliente no existe, no se puede registrar el pedido.';
    end if;
end//
delimiter ;

select * from  pedidos;
insert into pedidos(idCliente, fechaPedido, total) values(5, now(), 1599);
select * from pedidos;

# Ejercicio 3
delimiter //
create trigger hayStock
before insert on detallepedidos
for each row
begin
    declare stockExistente int default 0;
    select stock into stockExistente from productos where productos.idProducto = new.idProducto;
    if new.cantidad > stockExistente then
        signal sqlstate '45000'
        set message_text = 'No tenemos esta cantidad de dicho producto en stock';
    end if;
end//
delimiter ;

select * from  detallepedidos;
select * from productos;
insert into detallepedidos(idProducto, cantidad, precioUnitario) values(105, 25, 5000);

# Ejercicio 4
delimiter //
create trigger validarPrecio
before insert on detallepedidos
for each row
begin
    if (new.precioUnitario != (select precio from productos where productos.idProducto = new.idProducto)) then
        insert into auditoria (tablaafectada, evento, descripcion, usuario, fecha)
        values ('DetallePedidos', 'INSERT',
                concat('El precio del producto ', new.idProducto, ' no coincide con el precio actual.'), user(),now());
        signal sqlstate '45000'
        set message_text = 'El precio unitario no coincide con el original.';
    end if;
end //

drop trigger validarPrecio;
select * from  detallepedidos;
select * from auditoria;
insert into detallepedidos(idProducto, cantidad, precioUnitario) values(104, 5, 5000);

# Ejercicio 5
delimiter //
create trigger validarPromociones
before insert on detallepedidos
for each row
begin
    if (new.cantidad > 10) then
        insert into auditoria (tablaafectada, evento, descripcion,usuario, fecha)
        values ('DetallePedidos', 'INSERT',
                concat('Se aplicó una promoción por más de 10 unidades del producto ', new.idProducto, '.'), user(), now());
    end if;
end //
delimiter ;

drop trigger validarPromociones;
insert into detallepedidos(idProducto, cantidad, precioUnitario) values(104, 11, 4500);
select * from auditoria;

# Ejercicio 6
delimiter //
create trigger calcularTotal
after insert on DetallePedidos
for each row 
begin 
    declare found integer default 1 ;
    declare acumulado double default 0 ;
    declare v_cantidad int default 0 ;
    declare v_precioUnitario double default 0 ;
    declare detalleCursor cursor for
    select cantidad, precioUnitario from DetallePedidos where idPedido = new.idPedido ;
    declare continue handler for not found set found = 0 ;
    fetch detalleCursor into v_cantidad, v_precioUnitario ;
    open detalleCursor;
    while found = 1 do
        set acumulado = acumulado + (v_cantidad * v_precioUnitario) ;
        fetch detalleCursor into v_cantidad, v_precioUnitario ;
    end while ;
    close detalleCursor;
    update Pedidos set total = acumulado where idPedido = new.idPedido ;
end //
delimiter ;

insert into detallepedidos(idProducto, cantidad, precioUnitario) values(104, 10, 4500);
select * from auditoria;

# Ejercicio 7
delimiter //
create trigger actualizarStock
after insert on detallepedidos
for each row
begin
    update productos set stock = stock - new.cantidad where idproducto = new.idproducto;
end//
delimiter ;

insert into detallepedidos(idProducto, cantidad, precioUnitario) values(104, 10, 4500);
select * from productos;

# Ejercicio 8
delimiter //
create trigger pedidoAuditoria
after insert on pedidos
for each row
begin
    insert into auditoria (tablaafectada, evento, descripcion, usuario, fecha)
    values ('Pedidos', 'INSERT', concat('Pedido registrado con id: ', new.idpedido, ', total: ', new.total), user(), now());
end//
delimiter ;

# Ejercicio 9
delimiter //
create trigger registrarProductoEliminado
after delete on productos
for each row
begin
    insert into auditoria (tablaafectada, evento, descripcion, fecha)
    values ('productos', 'DELETE',
            concat('Producto eliminado: ID=', old.idProducto, ', Nombre=', old.nombre), now());
end;
delimiter ;

delete from productos where idProducto = 1;
select * from auditoria;

# Ejercicio 10
delimiter //
create trigger regresarStockProducto
after delete on detallepedidos
for each row
begin
    update productos
    set stock = stock + old.cantidad
    where idProducto = old.idProducto;
end;
delimiter ;

delete from detallepedidos where idDetalle = 1;
select * from productos where idProducto = (select detallepedidos.idProducto from detallepedidos where idDetalle = 1);

# Ejercicio 11
delimiter //
create trigger evitarEliminacionClientes
before delete on clientes
for each row
begin
    if exists (select 1 from pedidos where idCliente = old.idCliente) then
        signal sqlstate '45000'
        set message_text = 'No se puede eliminar el cliente porque tiene pedidos asociados.';
    end if;
end;
delimiter ;

delete from clientes where idCliente = 1;
select * from pedidos where idCliente = 1;

# Ejercicio 12
delimiter //
create trigger eliminarDetallesRestaurarStock
before delete on Pedidos
for each row
begin
    declare fin integer default 0 ;
    declare v_idProducto int ;
    declare v_cantidad int ;
    declare detalleCursor cursor for
    select idProducto, cantidad from DetallePedidos where idPedido = old.idPedido ;
    declare continue handler for not found set fin = 1 ;

    open detalleCursor ;
    fetch detalleCursor into v_idProducto, v_cantidad ;
    while fin = 0 do
        update Productos
        set stock = stock + v_cantidad
        where idProducto = v_idProducto ;
        delete from DetallePedidos
        where idPedido = old.idPedido and idProducto = v_idProducto ;
        fetch detalleCursor into v_idProducto, v_cantidad ;
    end while ;
    close detalleCursor ;
end //
delimiter ;

delete from Pedidos where idPedido = 1 ;
select * from DetallePedidos ;
select * from Productos ;

# Ejercicio 13
delimiter //
create trigger cambioPrecio
after update on productos
for each row
begin
    if old.precio <> new.precio then
        insert into auditoria (tablaafectada, evento, descripcion, fecha)
        values ('productos', 'UPDATE',
                concat('Cambio de precio: ID=', old.idProducto, ', Precio anterior=', old.precio, ', Nuevo precio=', new.precio), now());
    end if;
end;
delimiter ;

update productos set precio = 50.00 where idProducto = 1;
select * from auditoria;

# Ejercicio 14
delimiter //
create trigger ajustarCambioCantidad
after update on detallepedidos
for each row
begin
    if old.cantidad <> new.cantidad then
        update productos
        set stock = stock + (old.cantidad - new.cantidad)
        where idProducto = old.idProducto;
    end if;
end;
delimiter ;

update detallepedidos set cantidad = 5 where idDetalle = 1;
select * from productos;

# Ejercicio 15
delimiter //
create trigger cambioEmail
after update on clientes
for each row
begin
    if old.email <> new.email then
        insert into auditoria (tablaafectada, evento, descripcion, fecha)
        values ('clientes', 'UPDATE',
                concat('Cambio de email: ID=', old.idCliente, ', Email anterior=', old.email, ', Nuevo email=', new.email), now());
    end if;
end;
delimiter ;

update clientes set email = 'nuevoemail@ejemplo.com' where idCliente = 4;
select * from auditoria;

# Drops
drop trigger if exists nuevoCliente;
drop trigger if exists validadPedido;
drop trigger if exists hayStock;
drop trigger if exists validarPrecio;
drop trigger if exists validarPromociones;
drop trigger if exists calcularTotal;
drop trigger if exists actualizarStock;
drop trigger if exists pedidoAuditoria;
drop trigger if exists registrarProductoEliminado;
drop trigger if exists regresarStockProducto;
drop trigger if exists evitarEliminacionClientes;
drop trigger if exists eliminarDetallesRestaurarStock;
drop trigger if exists cambioPrecio;
drop trigger if exists ajustarCambioCantidad;
drop trigger if exists cambioEmail;