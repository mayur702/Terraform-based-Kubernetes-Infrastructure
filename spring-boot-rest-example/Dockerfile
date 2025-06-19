# ---------- Build Stage ----------
FROM maven:3.9.8-eclipse-temurin-8 AS builder

WORKDIR /app

# Copy Maven files and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy source and build
COPY src ./src
RUN mvn clean package -DskipTests

# ---------- Runtime Stage ----------
FROM eclipse-temurin:8-jdk

WORKDIR /app

# Copy WAR from build stage
COPY --from=builder /app/target/spring-boot-rest-example-0.5.0.war app.war

EXPOSE 8091

CMD ["java", "-jar", "app.war"]

