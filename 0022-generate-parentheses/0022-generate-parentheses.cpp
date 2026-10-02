class Solution {
public:
    vector<string> result;
    void iter(string s,int open,int close,int n)
    {
        if(open==n && close==n)
        {
            result.push_back(s);
            return;
        }
        if(open<n)
            iter(s+"(",open+1,close,n);
        if(close<open)
            iter(s+")",open,close+1,n);
    }
    vector<string> generateParenthesis(int n)
    {
        iter("",0,0,n);
        return result;
    }
};