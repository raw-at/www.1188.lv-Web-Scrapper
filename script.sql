CREATE TABLE company 
(id integer NOT NULL PRIMARY KEY auto_increment, 
category_id integer,company_name varchar(255),company_address varchar(255), 
email varchar(255),registration_no varchar(45),legal_address varchar(500))
ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;
create table categories
(category_id integer REFERENCES company(category_id) ON DELETE CASCADE ON UPDATE CASCADE,
category_name varchar(255)
)ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;
create table phones
(id integer NOT NULL PRIMARY KEY auto_increment,
company_id integer NOT NULL REFERENCES company (id) ON DELETE CASCADE ON UPDATE CASCADE, 
number varchar(45),phonetype varchar(255))ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;
create table products_companies
(company_id integer NOT NULL REFERENCES company(id) ON DELETE CASCADE ON UPDATE CASCADE,
product_id integer NOT NULL REFERENCES products(id) ON DELETE CASCADE ON UPDATE CASCADE)
ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;
create table products
(id integer NOT NULL PRIMARY KEY auto_increment,
product_name varchar(255))ENGINE=InnoDB DEFAULT CHARACTER SET=utf8;


CREATE INDEX company_id_index ON company (id);
CREATE INDEX product_id_index ON products (id);
CREATE INDEX phone_id_index ON phones (id);