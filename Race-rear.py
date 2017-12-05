
AimForLane( 0 )

Speed( 100 )

WaitForGo( )

while Globals.running :

    WaitForWaypoint( 2 )
    Speed( 70 )
    AimForLane( -2 )


    WaitForWaypoint( 3 )
    AimForLane( 0 )
    Speed( 100 )

    WaitForWaypoint( 4 )
    Speed(80)
    AimForLane( 2 )

    WaitForWaypoint( 7 )
    Speed(100)
    AimForLane( 0 )

    WaitForSeconds( 0.01 )


