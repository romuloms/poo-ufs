import tkinter as tk

def decimalToBinary():
    try:
        decimalNum = int(inputField.get())
        binaryNum = bin(decimalNum).replace("0b", "")
        outputLabel.config(text=f"Binary: {binaryNum}")
    except ValueError:
        outputLabel.config(text="Ivalid input. Enter a decimal number.")

def binaryToDecimal():
    try:
        binaryNum = inputField.get()
        decimalNum  = int(binaryNum, 2)
        outputLabel.config(text=f"Decimal: {decimalNum}")
    except ValueError:
        outputLabel.config(text="Invalid input. Enter a binary number.")

def clearOutput():
    outputLabel.config(text="")

root = tk.Tk()
root.title("Binary and Decimal converter")

menuFrame = tk.Frame(root)
menuFrame.pack()

clearButton = tk.Button(root, text="Clear", command=clearOutput)
clearButton.pack()

inputField = tk.Entry(root)
inputField.pack()

decToBinButton = tk.Button(menuFrame, text="Decimal to Binary", command=decimalToBinary)
decToBinButton.pack(side=tk.LEFT)

binToDecButton = tk.Button(menuFrame, text="Binary to Decimal", command=binaryToDecimal)
binToDecButton.pack(side=tk.LEFT)

outputLabel = tk.Label(root, text="", pady=10)
outputLabel.pack()

root.mainloop()