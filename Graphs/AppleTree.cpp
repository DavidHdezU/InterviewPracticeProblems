#include<bits/stdc++.h>
#include <iostream>
#include<cstdio>
using namespace std;
int nodes_in_tree(unordered_map<int, vector<int>> adj_list, vector<int> apples, int nodo){
    int res = 0;
    if(apples[nodo] == 1){
        res += 1;
    }
    stack<int> stack;
    stack.push(nodo);
    unordered_set<int> visitados;
    visitados.insert(nodo);
    
    while(!stack.empty()){ // DFS

        int v = stack.top();
        stack.pop();

        for(int u : adj_list[v]){
            if(visitados.find(u) == visitados.end()){
                if(apples[u] == 1){
                    res += 1;
                }
                visitados.insert(u);
                stack.push(u);
            }
        }
    }
    return res;

}
void count(){
    // 1. Creamos la lista adyacencia
    int N;
    cin >> N;
    unordered_map<int, vector<int>> adj_list;
    int u, v;
    vector<int> apples;
    for(int i = 0; i < N; i++){
        apples.push_back(1);
    }
    N -= 1;
    while(N--){
        cin >> u >> v;
        adj_list[u-1].push_back(v-1);
    }
    // 2 Leer Queries
    int M;
    cin >> M;
    char query;
    int nodo;
    
    while(M--){
        cin >> query >> nodo;
        
        if(query == 'C'){
            if(apples[nodo-1] == 1){
                apples[nodo-1] = 0;
            }else{
                apples[nodo-1] = 1;
            }
        }else{
            cout << nodes_in_tree(adj_list, apples, nodo-1) << endl;
        }
    }
}

int main(){
    count();
    return 0;
}
