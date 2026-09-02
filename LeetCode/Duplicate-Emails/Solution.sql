1select email as Email from Person
2group by email
3having count(email)>1;
4
5
6