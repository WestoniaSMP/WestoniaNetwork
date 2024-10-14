# Use itzg's Minecraft Server Docker image as base
FROM itzg/minecraft-server

# Install git, OpenJDK 21, Gradle, and curl
RUN apt-get update && apt-get install -y git openjdk-21-jdk gradle curl

# Set JAVA_HOME and add it to the PATH
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Set working directory for the initialization process
RUN mkdir /init
WORKDIR /init

# Clone the Westonia repository
# FIXME: For now, we are using the old Westonia project. This will be changed in the future.
# TODO: Change the repository URL to the new Westonia project: https://github.com/WestoniaSMP/Westonia.git
RUN git clone https://github.com/WestoniaSMP/Westonia-Hibernate.git

# Set working directory for the Westonia project
WORKDIR /init/Westonia-Hibernate

# Set permissions for the Gradle wrapper and build the plugin using Gradle
RUN ls
RUN chmod +x ./gradlew
RUN ./gradlew clean shadowJar

# Extract the version from build.gradle.kts for later use
#RUN VERSION=$(grep '^version =' build.gradle.kts | sed 's/version = "\(.*\)"/\1/') && \
#    echo "Plugin version: $VERSION"

# Set working directory for the plugins and copy the built plugin to the plugins directory
WORKDIR /plugins
#FIXME: For now, i am hardcoding the jar file name. This will be changed in the future.
#TODO: Change the hardcoded jar file name to the variable VERSION
RUN cp "/init/Westonia-Hibernate/build/libs/Westonia-Beta 1.0 MC1.21.1-DEV-all.jar" /plugins/