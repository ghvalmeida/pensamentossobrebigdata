
Twitter_1 = LOAD '/input/twitter' USING PigStorage(' ') AS (follower:int, followee:int);
Twitter_2 = LOAD '/input/twitter' USING PigStorage(' ') AS (follower:int, followee:int);
Twitter_3 = LOAD '/input/twitter' USING PigStorage(' ') AS (follower:int, followee:int);
/* 
DUMP Twitter_1;
*/

Twitter_SelfJoin = JOIN Twitter_1 by $1, Twitter_2 by $0;
/* 
DUMP Twitter_SelfJoin;
*/

Twitter_FullJoin = JOIN Twitter_3 by ($1, $0), Twitter_SelfJoin by ($0, $3);
/*
DUMP Twitter_FullJoin;
*/

Triangles = FILTER Twitter_FullJoin BY ($0 < $1 AND $1 < $3) OR ($0 > $1 AND $1 > $3);
/*
DUMP Triangles;
*/

Triangles_Grp = GROUP Triangles ALL;
Triangles_Cnt = FOREACH Triangles_Grp GENERATE COUNT(Triangles);

DUMP Triangles_Cnt;
