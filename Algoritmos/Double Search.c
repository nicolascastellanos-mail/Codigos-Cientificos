// April the 24th, 2023. 7:22 p.m

#include <stdio.h>
#include <time.h>

int iterations;

int dsearch(int list[], int size, int searched){
    extern int iterations;
    int left, right;

    iterations = 0;
    left = 0; right = size - 1;

    while(left != right){
        iterations++;
        if(list[left] == searched){
            return left;
        } else if (list[right] == searched){
            return right;
        }

        left++; right--;
    }

    return -1;
}

int qsearch(int list[], int size, int searched){
    extern int iterations;
    int leftl, leftc, rightc, rightr;

    iterations = 0;
    leftl = 0; leftc = size / 4; rightc = (size - 1) - (size / 4); rightr = size - 1;

    while(leftl != rightr){
        iterations++;
        if(list[leftl] == searched){
            return leftl;
        } else if(list[leftc] == searched){
            return leftc;
        } else if (list[rightr] == searched){
            return rightr;
        } else if (list[rightc] == searched){
            return rightc;
        }

        leftl++; leftc++; rightc--; rightr--;
    }

    return -1;
}

int linear(int list[], int size, int searched){
    extern int iterations;
    int index;

    iterations = 0;

    for(index = 0; index < size; index++){
        iterations++;
        if(list[index] == searched){
            return index;
        }
    }

    return -1;
}

int main(){
    int size;
    size = 20;

    // int list[10] = {5, 4, 2, 8, 9, 1, 3, 7, 6, 0};
    int list[20] = {5, 4, 2, 8, 9, 1, 15, 13, 14, 16, 12, 11, 19, 17, 18, 3, 7, 6, 0, 10};
    int searched;
    int* index;

    clock_t start = clock();

    printf("============================\n");
    printf("TESTING DOUBLE RUNNER SEARCH\n");
    printf("============================\n");
    printf("\n");

    extern int iterations;

    for(searched = 0; searched < size; searched++){
        if((index = dsearch(list, size, searched)) != -1){
            printf("The element %d was found in the index %d with %d iterations\n", searched, index, iterations);
        } else {
            printf("The element %d was not found\n", searched);
        }
    }

    printf("\n");
    printf("Execution time for dsearch: %f", ((double)clock() - start) / CLOCKS_PER_SEC);
    printf("\n");

    start = clock();

    printf("==========================\n");
    printf("TESTING QUAD RUNNER SEARCH\n");
    printf("==========================\n");
    printf("\n");

    for(searched = 0; searched < size; searched++){
        if((index = qsearch(list, size, searched)) != -1){
            printf("The element %d was found in the index %d with %d iterations\n", searched, index, iterations);
        } else {
            printf("The element %d was not found\n", searched);
        }
    }

    printf("\n");
    printf("Execution time for qsearch: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
    printf("\n");

    start = clock();

    printf("============================\n");
    printf("TESTING SINGLE RUNNER SEARCH\n");
    printf("============================\n");
    printf("\n");

    for(searched = 0; searched < size; searched++){
        if((index = linear(list, size, searched)) != -1){
            printf("The element %d was found in the index %d with %d iterations\n", searched, index, iterations);
        } else {
            printf("The element %d was not found\n", searched);
        }
    }

    printf("\n");
    printf("Execution time for linear: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
    printf("\n");

    return 0;
}

// Function dsearch finished at 7:40 p.m.

// Time counting implemented at 7:44 p.m.

// At 7:52 I extended the list up to 20 elements because I can't measure any time with 10

// At 7:54 I created the size variable

// Starting 7:55 p.m with other n-search functions

// At 7:59 p.m. after implementing qsearch I realize that CodeBlocks itself already measures the execution time cleaner

// Finished final testings and version of the program at 8:04 p.m.

// Conclusion of the experiment: the dsearch function is faster than the qsearch

// Starting experiment with linear search at 8:04 p.m.

// Finished the experiment at 8:28 p.m. after failing while trying to count the iterations

// Starting to try to count iterations again at 8:54 p.m.

// Just because I don't know how to return arrays, I used extern variables and successfully finished at 9:12 p.m.
