use Tienda;
# Ejercicio 1
create view VistaClientes as
select nombre as nombre_cliente, email as correo, fecha_registro as registro
from clientes where year(fecha_registro) = 2023;

select * from VistaClientes;

# Ejercicio 2
create view VistaDetallePedido as
select p.id_pedido as pedido_id, p.fecha_pedido as fecha, pr.nombre_producto as producto, dp.cantidad as cantidad_vendida, dp.precio_unitario, (dp.cantidad * dp.precio_unitario) as subtotal from pedidos p join detalles_pedido dp on p.id_pedido = dp.id_pedido join productos pr on dp.id_producto = pr.id_producto;

select * from VistaDetallePedido;

# Ejercicio 3
update clientes set nombre = 'Ana García' where email = 'ana@gmail.com';

select * from clientes;

# Ejercicio 4
create or replace view VistaClientes as
select nombre as cliente, fecha_registro as fecha_alta from clientes where year(fecha_registro) = 2023;

select * from VistaClientes;

# Ejercicio 5
drop view if exists VistaClientes;

# Ejercicio 6
create view VistaPedidos as
select c.nombre as cliente, p.fecha_pedido, p.total as monto_total from pedidos p join clientes c on p.id_cliente = c.id_cliente;

select * from VistaPedidos;

# Ejercicio 7
update pedidos set fecha_pedido = '2024-04-10' where id_cliente = (select id_cliente from clientes where nombre = 'Ana García');
select * from pedidos;
# Ejercicio 8
create index idxEmail on clientes(email);
select * from clientes;

# Ejercicio 9
explain select * from clientes where email = 'ana@gmail.com';

# Ejercicio 10
create index idxPedidoProducto on detalles_pedido(id_pedido, id_producto);

# Ejercicio 11
explain select * from detalles_pedido where id_pedido = 1 and id_producto = 2;

# Ejercicio 12
drop index idxEmail on clientes;

# Ejercicio 13
show full tables where table_type = 'VIEW';

# Ejercicio 14
show indexes from detalles_pedido;