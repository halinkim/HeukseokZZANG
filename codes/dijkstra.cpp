
int v,e,st; //정점의 개수, 간선의 개수, 시작 위치 

// {비용, 정점 번호}
vector<pair<int,int>> adj[MAX_SIZE]; //adj[i].push_back({w,x}) 면 i->x 이고 거리는 w 
const int INF = 0x3f3f3f3f;
int d[MAX_SIZE]; // 최단 거리 테이블
  fill(d,d+v+1,INF);
  while(e--){
    int u,x,w;
    adj[u].push_back({w,x});
  }

  priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;
  d[st] = 0;
  // 우선순위 큐에 (0, 시작점) 추가
  pq.push({d[st],st});
  while(!pq.empty()){
    auto cur = pq.top(); pq.pop(); // {비용, 정점 번호}    
    // 거리가 d에 있는 값과 다를 경우 넘어감
    if(d[cur.second] != cur.first) continue;
    for(auto nxt : adj[cur.second]){ //이웃하는 모든 노드들 = nxt에 대하여 반복 
      if(d[nxt.second] <= d[cur.second]+nxt.X) continue;
      // cur를 거쳐가는 것이 더 작은 값을 가질 경우
      // d[nxt.Y]을 갱신하고 우선순위 큐에 (거리, nxt.Y)를 추가
      d[nxt.second] = d[cur.second]+nxt.first;
      pq.push({d[nxt.second],nxt.second});
    }
  
