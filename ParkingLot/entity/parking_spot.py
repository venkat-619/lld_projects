
class ParkingSpot:

    def __init__(self, spot_id: str):
        self._spot_id = spot_id
        self.is_free = True


    def occupy_spot(self) -> None:
        '''
            Occupying spot by flagging it false
        '''
        self.is_free = False
    
    def release_spot(self) -> None:
        '''
            Releasing spot by flagging it True
        '''
        self.is_free = True

    @property
    def spot_id(self) -> str:
        '''
            Returning spot id read only access to spot id.
        '''
        return self._spot_id