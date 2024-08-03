import time
import os


# Function to get the current chunk coordinates from the player's coordinates
def get_chunk_coordinates(player_x, player_z):
    chunk_x = player_x // 16
    chunk_z = player_z // 16
    return chunk_x, chunk_z


# Function to log chunk coordinates to a file and print to console
def log_chunk_coordinates(file_path):
    visited_chunks = set()  # To avoid duplicate entries
    player_x, player_z = 0, 0  # Starting coordinates

    with open(file_path, 'a') as file:
        try:
            while True:
                chunk_x, chunk_z = get_chunk_coordinates(player_x, player_z)
                chunk = (chunk_x, chunk_z)

                if chunk not in visited_chunks:
                    visited_chunks.add(chunk)
                    log_entry = f"Chunk visited: ({chunk_x}, {chunk_z})\n"
                    print(log_entry, end='')  # Print to console
                    file.write(log_entry)  # Log to file

                # Simulate more realistic movement
                player_x += 10  # Move to the next chunk incrementally
                player_z += 10  # Move to the next chunk incrementally

                time.sleep(5)  # Log every 5 seconds
        except KeyboardInterrupt:
            print("\nLogging stopped.")
            file.close()


if __name__ == "__main__":
    log_file_path = os.path.join(os.path.dirname(__file__), "chunk_visits.txt")
    log_chunk_coordinates(log_file_path)
