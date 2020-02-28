
# logs analysis:

The objective of the Logs Analysis Project is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

#make configuration for virtual machine

1-download virtual box https://www.virtualbox.org/wiki/Downloads
2-download vagrant https://www.vagrantup.com/
3-download virtual machine
4-download database newsdata
1-cd /path/to/vagrant
5-copy newdata.sql to vagrant 

 
# steps
```
1-cd/path/to/vagrant
```
   vagrant up
   ```
   vagrant provision
   ```
   ```
   vagrant ssh
   ```
```
2-cd /vagrant 
```
```
3-psql -d news -f newsdata.sql
```


 

# run reporting tool
1-cd /path/to/vagrant
vagrant up
vagrant ssh

2-cd /vagrant 
3- python style.py
 
#functions used:
select 
where
count
limit
group by
order  by
etc

author sabreen salama elsayed 
