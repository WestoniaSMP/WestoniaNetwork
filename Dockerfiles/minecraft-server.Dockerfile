# Use itzg's Docker image for Minecraft server, with Folia as the base image
FROM itzg/minecraft-server

# Install Git, OpenJDK 17, and Gradle
RUN apt-get update && apt-get install -y git openjdk-17-jdk gradle

# Set the working directory for the plugins
WORKDIR /plugins

# Clone the Westonia plugin from GitHub
RUN git clone https://github.com/WestoniaSMP/Westonia.git

# Set the working directory for the Westonia source code
WORKDIR /plugins/Westonia
RUN git pull origin main

RUN gradle clean shadowJar

RUN cp build/libs/Westonia /data/plugins/

# Startbefehl für den Minecraft-Server
CMD ["start"]