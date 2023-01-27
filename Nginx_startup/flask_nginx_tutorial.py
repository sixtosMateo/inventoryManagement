'''
NGINX

- nginx is a fast, production level HTTP level
- when serving your application with one of the WSGI servers it's good or necessary
to put a dedicated HTTP server in front of it
- This 'reverse proxy' can handle incoming requests, TLS and other security and
performance concerns better than the WSGI server

Installing and running Nginx itself is outside the scope of this tutorial

- this tutorial outlines the basics of configuring NGINX to proxy your application

Domain Name

In general you will pay for a domain name from a registrar, pay for server space
with a hosting provider and then point your registrar at the hosting provider's
name servers

To simulate this you can also edit your hosts file located at /etc/hosts on Linux
add a line that associates a name with the local IP

Modern Linux systems may be configured to treat any domain name that ends with
.localhost like this with out adding it to the host file

/etc/hosts
127.0.0.1 hello.localhost


Configuration

The nginx configuration is located at /etc/nginx/nginx.conf on Linux.
Its different on different operating systems. Check docs and look for nginx.conf

Remove or comment out any existing server section. Add a server section and use
a proxy_pass directive to point to the address the WSGI server is listening on

For this example we will assume that the WSGI server is listening locally at
http://127.0.0.1:8000.


/etc/nginx.conf
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Prefix /;
    }
}

Then tell Flask it is behind a Proxy so that your application uses these headers
'''

'''
How do you tell Flask that it is behind a proxy ?


'''
