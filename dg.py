a={
'D' : ('*******    ','*      *   ','*       *  ','*        * ','*         *','*        * ','*       *  ','*      *   ','*******    '),
'G' : ('   ******  ','  *        ',' *         ','*          ','*    ***** ','*        * ',' *       * ','  *      * ','   ******  '),
}
name = raw_input('please enter dg: ').upper()
for i in range(0,9):
    for o in name:
	    print a[o][i],
    print ''