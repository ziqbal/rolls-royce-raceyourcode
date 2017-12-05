

WaitForGo( )

AimForLane( -1 )
Speed( 100 )

while Globals.running :

    WaitForWaypoint( 2 )

    AimForLane( 1 )
    Speed( 80 )


    WaitForWaypoint( 3 )

    AimForLane( -1 )
    Speed( 100 )


    WaitForWaypoint( 6 )

    AimForLane( 1 )
    Speed( 100 )

    WaitForWaypoint( 9 )

    AimForLane( -1 )
    Speed( 100 )


    #WaitForWaypoint( 2 )
    #Speed( 70 )
    #AimForLane( 2 )


    #WaitForWaypoint( 3 )
    #AimForLane( 0 )
    #Speed( 100 )

    #WaitForWaypoint( 4 )
    #Speed(80)
    #AimForLane( 1 )




    #WaitForWaypoint( 9 )
    ##Speed(100)
    #AimForLane( 0 )

    WaitForSeconds( 0.01 )


