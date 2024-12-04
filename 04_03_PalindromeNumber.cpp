class Solution {
public:
    bool isPalindrome(int x) {
        int number = x;
        long reverse = 0;
        while(x > 0) {
            reverse = reverse*10 + x%10;
            x = x / 10;
        }
        if(number == int(reverse)) {
            return true;
        } else {
            return false;
        }
    }
};
