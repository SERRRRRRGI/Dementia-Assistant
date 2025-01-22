import numpy as np
import msgpack

def encode_data(**kwargs):
    """
    Encodes the provided data into a format suitable for msgpack serialization.
    Specifically, NumPy arrays are converted to bytes, and other types are passed through unchanged.
    
    Args:
        **kwargs: Keyword arguments with data to encode.
    
    Returns:
        bytes: A msgpack serialized byte stream of the data.
    """
    encoded = {}
    for key, value in kwargs.items():
        if isinstance(value, np.ndarray):
            # Convert NumPy arrays to bytes and store the shape, dtype
            encoded[key] = {
                'type': 'ndarray',
                'data': value.tobytes(),
                'shape': value.shape,
                'dtype': str(value.dtype)
            }
        else:
            # Non-NumPy data passed as is
            encoded[key] = value
    
    # Use msgpack to pack the encoded dictionary into a byte stream
    return msgpack.packb(encoded)

def decode_data(encoded_data):
    """
    Decodes the received msgpack serialized data, converting bytes back to NumPy arrays where applicable.
    
    Args:
        encoded_data (bytes): A msgpack byte stream to decode.
    
    Returns:
        dict: A dictionary with decoded data (NumPy arrays and other variables).
    """
    decoded = {}
    # Unpack the msgpack byte stream back into a dictionary
    unpacked_data = msgpack.unpackb(encoded_data)
    
    for key, value in unpacked_data.items():
        if isinstance(value, dict) and value.get('type') == 'ndarray':
            # Convert back to NumPy array from bytes
            decoded[key] = np.frombuffer(value['data'], dtype=value['dtype']).reshape(value['shape'])
        else:
            # Non-NumPy data passed as is
            decoded[key] = value
    
    return decoded