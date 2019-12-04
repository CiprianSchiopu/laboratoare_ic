LDFLAGS=-L/mnt/c/Users/a-rarad/Desktop/openssl-1.1.1d/openssl/lib -lcrypto
CFLAGS=-Wall -g -I/mnt/c/Users/a-rarad/Desktop/openssl-1.1.1d/openssl/include

.PHONY: all
all: birthday

birthday: birthday.o
	gcc -o $@ $< $(LDFLAGS)

.PHONY: clean
clean:
	rm -vf *.o birthday
