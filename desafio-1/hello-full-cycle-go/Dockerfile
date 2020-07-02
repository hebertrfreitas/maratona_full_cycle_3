FROM golang:1.14

WORKDIR /go/src/app
COPY . .
RUN ls
RUN go install
RUN ls /go/bin

ENTRYPOINT /go/bin/app


