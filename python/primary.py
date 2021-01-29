DM[];
DG[];

Directed- Graph-Matrix()
{
    for (i=0; i<n; i++)
        for (k= each attribute that composed determinant key i)
            for ( j=0; j<n ; j++) {
                if ( DM[j][k]!=0 && DG[j][i]!=-1)
                    DG[j][i]=1;
                else DG[j][i]=-1; }
}

Dependency-closure ()
{
    for (i=0; i<n ; i++)
        for( j=0; j<n ; j++)
            if( i!=j && Path[i][j]!=-1) {
                for (k=0; k<m ; k++)
                    if( DM[j][k]!=0 && DM[j][k]!=2)
                    DM[i][k]=j; }
}

Circular-Dependency ()
{
    for ( i=0; i<n; i++)
        for(j=0; j<m; j++)
            if(DM[i][j]!= {0,1,2})
                if(FindOne (i, j, j, n)&& DM2[i][j]==1)
                DM[i][j]=1;
}

int FindOne (int i, element j, int k, int n)
{
    if(DM[j][k]==1 && n>=1)
        return 0;
    else if (n<1)
        return 1;
    else
        return FindOne (i, DM[i][k], k, n-1);
}
