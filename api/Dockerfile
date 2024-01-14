#FROM eclipse-temurin:17-jdk-alpine
#ENTRYPOINT ["java","-jar","/message-server-1.0.0.jar"]
FROM gradle
WORKDIR /app
COPY . .
CMD ["/app/run.sh"]
EXPOSE 8081
