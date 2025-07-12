#!/bin/bash
# Deploy Java app
cd /home/ec2-user/app
nohup java -jar eureka-server-0.0.1-SNAPSHOT.jar > app.log 2>&1 &