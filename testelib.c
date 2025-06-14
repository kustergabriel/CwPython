#include <stdio.h>


void hello_world();

__declspec(dllexport) void hello() {
    printf("Hello from C!\n");
}

