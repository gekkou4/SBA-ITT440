

import socket

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set the server address and port
    server_address = ('192.168.10.128', 406)
    
    # Get the number from the user
    number = int(input('Input your number: '))
    
    # Send the number to the server
    client_socket.sendto(str(number).encode(), server_address)
    
    # Receive the response from the server
    response, _ = client_socket.recvfrom(1024)
    is_prime_number = response.decode() == 'True'
    
    print(f'I know {number} is prime: {is_prime_number}')
    
    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    main()
