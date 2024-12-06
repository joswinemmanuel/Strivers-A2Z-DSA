class Solution {
  public:
    // Complete this function
    void printNos(int n) {
        // Your code here
        if(n > 0) {
            printNos(n - 1);
            cout << n << " ";
        }
        return;
    }
};
