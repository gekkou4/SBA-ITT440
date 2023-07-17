#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <signal.h>

#define NUM_CHILDREN 3

int pipefd[NUM_CHILDREN][2];
pid_t child_pid[NUM_CHILDREN];

void interrupt_handler(int signal) {
    printf("\nInterrupt signal received by child process. Exiting child process.\n");
    exit(EXIT_SUCCESS);
}

int main() {
    // Create pipes for communication
    for (int i = 0; i < NUM_CHILDREN; i++) {
        if (pipe(pipefd[i]) == -1) {
            perror("pipe");
            exit(EXIT_FAILURE);
        }
    }

    // Fork child processes
    for (int i = 0; i < NUM_CHILDREN; i++) {
        child_pid[i] = fork();

        if (child_pid[i] == -1) {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (child_pid[i] == 0) {
            // Child process
            close(pipefd[i][1]); // Close write end of the pipe

            signal(SIGINT, interrupt_handler); // Set up interrupt signal handler for the child

	    sleep (5); //Added delay for Ctrl-C command

            char child_message[256];
            int nbytes = read(pipefd[i][0], child_message, sizeof(child_message));
            printf("Child %d received message from parent: %s\n", getpid(), child_message);

            close(pipefd[i][0]); // Close read end of the pipe
            exit(EXIT_SUCCESS);
        } else {
            // Parent process
            close(pipefd[i][0]); // Close read end of the pipe

            char parent_message[256];
            sprintf(parent_message, "Hello Child %d, Welcome!", i + 1);

            write(pipefd[i][1], parent_message, strlen(parent_message) + 1);

            close(pipefd[i][1]); // Close write end of the pipe
        }
    }

    // Parent process
    printf("Parent process: Waiting for child processes to complete...\n");
    fflush(stdout);

    // Set up interrupt signal handler for the parent
    signal(SIGINT, interrupt_handler);

    // Wait for all child processes to complete
    for (int i = 0; i < NUM_CHILDREN; i++) {
        waitpid(child_pid[i], NULL, 0);
    }

    printf("Parent process: All child processes have completed.\n");

    return 0;
}
