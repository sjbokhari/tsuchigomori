FROM alpine:3.16.0
COPY build/main /main
RUN chmod +x /main

# Create start.sh file for wrapper Dockerfile to execute.
# This file contains the startup command for the service.
RUN echo -e "\
/main\n\
" > /start.sh \
RUN chmod +x /start.sh
EXPOSE 6000