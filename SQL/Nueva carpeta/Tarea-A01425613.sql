use Library;

# 1.
delimiter //
create procedure FindBooksByAuthor (in nombre varchar(100))
begin
    select b.title
    from Books b join Authors a on b.author_id = a.author_id where a.name = nombre;
end //
delimiter ;

select * from Authors;
call FindBooksByAuthor('Gabriel García Márquez');

# 2.
delimiter //
create procedure RegisterLoan (in idBook int, in idUser int)
begin
    insert into Loans (book_id, user_id, loan_date, return_date)
    values (idBook, idUser, NOW(), NULL);
end //
delimiter ;

select * from Loans;
call RegisterLoan(1, 2);

# 3.
delimiter //
create procedure  CountBooksByAuthor (in idAuthor int, out countBooks int)
begin
    select count(*) into countBooks from Books where author_id = idAuthor;
end //
delimiter ;

select * from Authors;
call CountBooksByAuthor(1, @countBooks);
select @countBooks;

# 4.
delimiter //
create procedure GetLoanInfo (in idLoan int, out bookTitle varchar(200), out userName varchar(100), out loanDate date)
begin
    select b.title, u.name, l.loan_date into bookTitle, userName, loanDate
    from Loans l join Books b on l.book_id = b.book_id join Users u on l.user_id = u.user_id where l.loan_id = idLoan;
end //
delimiter ;

call GetLoanInfo(1, @bookTitle, @userName, @loanDate);
select @bookTitle, @userName, @loanDate;

# 5.
delimiter //
create procedure UpdatePublicationYear (in bookID int, in pubYear int, out updatedYear int)
begin
    if pubYear < 1900 then
        set pubYear = 1900;
    end if;
    update Books set publication_year = pubYear where book_id = bookID;
    set updatedYear = pubYear;
end //
delimiter ;

call UpdatePublicationYear(1, 1890, @updatedYear);
select @updatedYear;

# 6.
delimiter //
create procedure ListActiveLoans ()
begin
    select b.title, u.name, l.loan_date
    from Loans l join Books b on l.book_id = b.book_id join Users u on l.user_id = u.user_id where l.return_date is null;
end //
delimiter ;

# 7.
delimiter //
create procedure ListBooksAndAuthors ()
begin
    select b.title, a.name
    from Books b join Authors a on b.author_id = a.author_id;
end //
delimiter ;

# 8.
delimiter //
create procedure calculatefine (in loanid int, out fineamount int)
begin
    declare dayslate int;
    set dayslate = datediff(now(), (select loan_date from loans where loan_id = loanid)) - 15;
    set fineamount = if(dayslate > 0, 10, 0);
end //
delimiter ;

select * from loans;
call calculatefine(1, @fineamount);
select @fineamount;

# 9.
delimiter //
create procedure classifybook (in bookid int)
begin
    declare publicationyear int;
    select publication_year into publicationyear from books where book_id = bookid;
    if publicationyear < 1950 then
        select 'clásico' as classification;
    else
        select 'moderno' as classification;
    end if;
end //
delimiter ;

select * from books;
call classifybook(1);

# 10.
delimiter //
create procedure GenerateMassiveLoans (in userid int, in n int)
begin
    declare i int default 0;
    declare randombookid int;
    declare books_cursor cursor for select book_id from books order by rand() limit n;

    open books_cursor;
    read_loop: loop
        fetch books_cursor into randombookid;
        if i >= n then
            leave read_loop;
        end if;
        insert into loans (book_id, user_id, loan_date, return_date) values (randombookid, userid, curdate(), null);
        set i = i + 1;
    end loop;
    close books_cursor;
end //
delimiter ;

select * from loans;
call generatemassiveloans(2, 5);
select * from loans where user_id = 2;

# 11.
delimiter //
create procedure updatepublicationyears ()
begin
    update books set publication_year = publication_year + 5 where publication_year < 2000;
end //
delimiter ;

select * from books;
call updatepublicationyears();
select * from books;

# 12.
delimiter //
create procedure ListAuthorsWithBooks ()
begin
    declare done int default 0;
    declare authorname varchar(100);
    declare bookcount int;
    declare authorcursor cursor for
        select a.name, count(b.book_id)
        from Authors a
        left join Books b on a.author_id = b.author_id
        group by a.author_id;

    declare continue handler for not found set done = 1;

    open authorcursor;
    read_loop: loop
        fetch authorcursor into authorname, bookcount;
        if done then
            leave read_loop;
        end if;
        select authorname, bookcount;
    end loop;

    close authorcursor;
end //
delimiter ;

select * from authors;
call listauthorswithbooks();

# 13.
delimiter //
create procedure markloansasreturned ()
begin
    declare done int default 0;
    declare loanid int;
    declare loancursor cursor for
        select loan_id from loans where return_date is null;
    declare continue handler for not found set done = 1;
    open loancursor;
    read_loop: loop
        fetch loancursor into loanid;
        if done then
            leave read_loop;
        end if;
        update loans
        set return_date = curdate()
        where loan_id = loanid;
    end loop;
    close loancursor;
end //
delimiter ;

select * from loans where return_date is null;
call markloansasreturned();
select * from loans where return_date is not null;

# Ángel Alexander Báez Flores | A01425613