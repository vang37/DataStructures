###Three Examples of Life-Critical Software Applications:
#
##Medical Device Software:
#Example: Software used in pacemakers or insulin pumps.
#Description: These devices monitor and regulate critical physiological functions. The 
#    software must operate with high reliability and precision to ensure patient safety.
##Aviation Control Systems:
#Example: Air Traffic Control (ATC) systems or Flight Management Systems (FMS).
#Description: These systems are responsible for managing aircraft navigation and ensuring 
#    safe separation between aircraft. Failures or errors can have catastrophic consequences.
##Automotive Safety Systems:
#Example: Advanced Driver Assistance Systems (ADAS) such as automatic braking or lane-keeping assist.
#Description: These systems enhance vehicle safety by providing real-time responses to road 
#    conditions and driver actions, preventing accidents and improving overall road safety.
#
###Example of Software Adaptability Impacting Sales vs. Bankruptcy:
#Software Application: Enterprise Resource Planning (ERP) Systems
#Example: SAP S/4HANA or Oracle ERP Cloud
#Description: ERP systems need to be adaptable to different industries and business processes. 
#    A vendor that can quickly customize and integrate their ERP system to meet specific needs 
#    of various sectors (such as manufacturing, retail, or healthcare) will remain competitive 
#    and increase sales. Conversely, a rigid ERP system that cannot adapt to changing customer 
#    requirements may lead to loss of clients and potential bankruptcy.
#
###Component from a Text-Editor GUI and its Methods:
#Component: TextArea (or TextBox)
#Methods:
#-setText(text: str): Sets the content of the text area to the provided string.
#-getText() -> str: Returns the current content of the text area.
#-appendText(text: str): Appends the provided string to the end of the current content.
#-clear(): Clears the content of the text area.
#-setFont(font: str): Sets the font type used in the text area.
#-setFontSize(size: int): Sets the font size used in the text area.
#-setTextColor(color: str): Sets the color of the text.
#
###Python Class Flower:

class Flower:
    def __init__(self, name: str, num_petals: int, price: float):
        """Initialize a new Flower instance.
        
        Args:
            name (str): The name of the flower.
            num_petals (int): The number of petals on the flower.
            price (float): The price of the flower.
        """
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def set_name(self, name: str):
        """Set the name of the flower.
        
        Args:
            name (str): The new name of the flower.
        """
        self._name = name

    def get_name(self) -> str:
        """Get the name of the flower.
        
        Returns:
            str: The name of the flower.
        """
        return self._name

    def set_num_petals(self, num_petals: int):
        """Set the number of petals on the flower.
        
        Args:
            num_petals (int): The new number of petals.
        """
        self._num_petals = num_petals

    def get_num_petals(self) -> int:
        """Get the number of petals on the flower.
        
        Returns:
            int: The number of petals on the flower.
        """
        return self._num_petals

    def set_price(self, price: float):
        """Set the price of the flower.
        
        Args:
            price (float): The new price of the flower.
        """
        self._price = price

    def get_price(self) -> float:
        """Get the price of the flower.
        
        Returns:
            float: The price of the flower.
        """
        return self._price

# Example usage
if __name__ == "__main__":
    flower = Flower("Rose", 32, 12.99)
    print("Flower name:", flower.get_name())
    print("Number of petals:", flower.get_num_petals())
    print("Price:", flower.get_price())

    flower.set_name("Tulip")
    flower.set_num_petals(6)
    flower.set_price(8.49)
    print("\nUpdated flower details:")
    print("Flower name:", flower.get_name())
    print("Number of petals:", flower.get_num_petals())
    print("Price:", flower.get_price())

