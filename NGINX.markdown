# NGINX
#recipe
## Take down a webpage and replace with page under construction
- [ ] Comment out all location blocks in the nginx configuration file
- [ ] Ensure that the following directives exist:

```
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    server_name hukev.com;
    root /var/www;
    index index.html index.htm;
}
```
- [ ] `sudo nginx -s reload`
