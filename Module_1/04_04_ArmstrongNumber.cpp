#include <iostream>
#include <math.h>

bool isArmstrong(int n) {
    int number = n;
    int sum = 0;
    int length = 0;
    
    while(number > 0) {
        length++;
        number /= 10;
    }
    
    number = n;
    while(number > 0) {
        sum += pow(number%10, length);
        number /= 10;
    }
    
    if(sum == n) {
        return true;
    } else {
        return false;
    }
}

int main() {
    std::cout << isArmstrong(153);
    return 0;
}
