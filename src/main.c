#include <stdlib.h>
#include <stdio.h>

#include <stddef.h>

typedef struct {
    int* start;
    int* end;
    int* capacity;
} DynamicArray;

void DynamicArray_init(DynamicArray* arr) {
    int* start = malloc(16 * sizeof(int));
    if(start == NULL) {
        fprintf(stderr, "malloc failed!!");
        exit(EXIT_FAILURE);
    }

    arr->start = start;
    arr->end = start;
    arr->capacity = start + 16;
}

ptrdiff_t DynamicArray_num_elements(const DynamicArray* arr) { return arr->end - arr->start; }

inline void DynamicArray_pop_UNSAFE(DynamicArray* arr) {
    arr->end--;
}
void DynamicArray_pop(DynamicArray* arr) {
    if(arr->start == arr->end) {
        fprintf(stderr, "Can't pop element");
        exit(EXIT_FAILURE);
    }
    DynamicArray_pop_UNSAFE(arr);
}


inline int DynamicArray_popReturnValue_UNSAFE(DynamicArray* arr) {
    arr->end--;
    return *(arr->end);
}
int DynamicArray_popReturnValue(DynamicArray* arr) {
    if(arr->start == arr->end) {
        fprintf(stderr, "Can't pop element");
        exit(EXIT_FAILURE);
    }
    return DynamicArray_popReturnValue_UNSAFE(arr);
}


inline int DynamicArray_getByIndex_UNSAFE(const DynamicArray* arr, const size_t idx) { return *(arr->start+idx);}
int DynamicArray_getByIndex(const DynamicArray* arr, const size_t idx) {
    if(idx > DynamicArray_num_elements(arr)) {
        fprintf(stderr, "DynamicArray_getByIndex got too large an index.");
        exit(EXIT_FAILURE);
    }
    return DynamicArray_getByIndex_UNSAFE(arr, idx);
}



int main(void) {
    printf("Hello, World!\n");
    DynamicArray arr;
    DynamicArray_init(&arr);

    printf("%p->%p (%p)", arr.start, arr.end, arr.capacity);

    printf("Number of elements = %ld", DynamicArray_num_elements(&arr));

    return EXIT_SUCCESS;
}