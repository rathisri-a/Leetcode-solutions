1select p.lastName,p.firstName,a.city,a.state
2FROM Person p
3LEFT JOIN Address a
4ON p.personId=a.personId;
5