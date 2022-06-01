# Spotify downloader for docker


### Steps
1. Git clone
```
$ git clone git@github.com:hellomyzn/spotipy-dl.git
```
2. Move to this
``` 
$ cd spotipy-dl
```
3. Copy .env file
```
$ cp .env.template .env
```
4. Update your credentials on `.env`. if you don’t have them, get them at [link](https://developer.spotify.com/my-applications)
```
$ vi .env
```
5. Run download command
```
$ sd url
# e.g.
$ sd https://open.spotify.com/track/0j8c2BHYZpkBBNazmSSy4n?si=f5d07bbf837546e8
```
6. Check songs out on `backend/downloads`

### Usage
#### Download multiple urls at onece
1. md -m
2. add urls through vim
![image](https://user-images.githubusercontent.com/20104403/171386955-710d52d8-4c1e-40ee-8f96-98e033702902.png)
3. Check songs out on `backend/downloads`

### Docker Command
```
# build
$ docker-compose up -d --build

# down
$ docker-compose down
```

### Into to container
```
# python3 server
$ docker-compose exec python3 bash
```

### test
```
# Hello world
$ docker compose exec python3 python src/sample.py
```

### Ruine the world
```
$  docker-compose down --rmi all --volumes --remove-orphans 
```
