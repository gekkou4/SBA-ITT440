import socket

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to a specific IP address and port
    server_address = ('', 406)
    server_socket.bind(server_address)
    
    print('On port 406, the server is listening...')
    
    while True:
        # Receive the number from the client
        data, client_address = server_socket.recvfrom(1024)
        number = int(data.decode())
        
        # Check if the number is prime
        is_prime_number = is_prime(number)
        
        # Prepare the response message
        response = str(is_prime_number).encode()
        
        # Send the response back to the client
        server_socket.sendto(response, client_address)
        
        print(f'Client has this {client_address}: {is_prime_number}')
    
    # Close the socket
    server_socket.close()

if __name__ == '__main__':
    main()
