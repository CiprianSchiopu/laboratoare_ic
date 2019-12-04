#include <openssl/sha.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

/* We want a collision in the first 4 bytes = 2^16 attempts */
#define N_BITS  16

int raw2int4(unsigned char * digest) {
    int i;
    int sum = 0;

    for (i = 0; i < 3; i++) {
        sum += sum * 256 + digest[i];
    }

    return sum;
}

void hexdump(unsigned char * string, int length) {
    int i;
    for (i = 0; i < length; i++) {
        printf("%02x", string[i]);
    }
}

int main(int argc, char * argv[]) {
    //uint32_t attempt;     /* Iterate through 16 bits of the 32; use the rest to run different attacks */
    unsigned char md[20]; /* SHA-1 outputs 160-bit digests */

    /* Try to find a collision on the first 4 bytes (32 bits) */
    unsigned int number_of_tries = 2 << N_BITS;
    unsigned int i, j;

    char ** random_messages = (char**) malloc(number_of_tries * sizeof(char *));
    int * random_hashes = (int *) calloc(number_of_tries, sizeof(int));

    /* Step 1. Generate 2^16 different random messages */
    for (int i = 0; i < number_of_tries; i++)
    {
        char * m = malloc(16 * sizeof(char));
        random_messages[i] = m;
    }

    /* Step 2. Compute hashes */
    SHA_CTX context;
    SHA1_Init(&context);
    for (int i = 0; i < number_of_tries; i++)
    {
        char *m = random_messages[i];

        SHA1_Update(&context, m, 16);
        SHA1_Final(md, &context); /* md must point to at least 20 bytes of valid memory */

        random_hashes[i] = raw2int4(md);
    }

    for (i = 0; i < number_of_tries; i++)
    {
        for (j = i + 1; j < number_of_tries; j++)
        {
            /* Step 3. Check if there exist two hashes that match in the first four bytes */
            if ((memcmp(random_messages[i], random_messages[j], 4) != 0) && (random_hashes[i] == random_hashes[j]))
            {
                /* Step 3a. If a match is found, print the messages and hashes */
                printf("%s has the same has as %s \n", random_messages[i], random_messages[j]);
            }
        }
    }

    return 0;
}
