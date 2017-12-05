
AimForLane( 0 )
Speed( 100 )

WaitForGo( )




while Globals.running :

    WaitForWaypoint( 2 )
    Speed(80)
    #AimForLane( 1 )


    WaitForWaypoint( 3 )
    Speed(100)

    WaitForWaypoint( 4 )
    Speed(80)

    WaitForSeconds( 0.01 )


