В случае, если у вас отсутствует `runtime: nvidia`, добавить GPU в сервис можно, заменив эту строчку в docker-compose.yaml на это:
```
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: 1
          capabilities: [gpu]
```
