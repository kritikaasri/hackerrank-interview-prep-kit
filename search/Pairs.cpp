#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long int n, k, p, count=0;
    cin>>n>>k;
    long long int s[n];
    for(long long int i=0;i<n;i++) cin>>s[i];
    sort(s,s+n);
    for(long long int it=0;it<n;it++) if(binary_search(s+(it+1),s+n,s[it]+k)) count++;
    cout<<count<<endl;
}
