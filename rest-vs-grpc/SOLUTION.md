
|   Method 	    | 	Local  	| Same-Zone  	|  Different Region 	|
|  	---	---		|	------	|	-------		|	--------------		|
|   REST add	|	3.678	|	  2.949		|  		279.807			|
|   gRPC add	|   0.403	|     0.414		|    	140.508			|
|   REST img	|   4.408	|     7.889		|	    1158.814	 	|
|   gRPC img	|   6.296   |     6.959		|		160.567		   	|
|   PING        |   0.058  	|     0.355		| 		139.879		    |


You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

OBSERVATION:
Fom the above table we see that REST is slower than gRPC APIs. The main reason being REST creats a new TCP connection for each request it receives but gRPC makes use of the same connection for all the requests. We see that the time taken by localhost and same-Zone VMs were very comparable. That being said, There was a slight increase in the time taken of REST Image api. This could be because Images had to be sent in seperate TCP connection to a different machine. There was a huge increase seen in time taken when client-server were in  different region. Ping time also increased.This is because of the network latency.  Ping time in this case is comparable with gRPC API. The client request has to travel all the way to US from EU. Hence Inter-region latency and REST having to establish new connections for each request leads to increaced latency. 