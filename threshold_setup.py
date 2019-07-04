from settings import *
from data_structures import *
from threshold_crypto import ThresholdCrypto
from threshold_crypto import number
import nacl.utils
import nacl.secret
import nacl.encoding
import nacl.exceptions
import nacl.hash

"""
USAGE

> #Generate threshold keys
> threshold_keys = threshold();
> message = 'Encr this mess'
> #Encrypt message with threshold public key
> encrypted_message = elgamal_enc_threshold(threshold_keys.pk, message)
> #Get array of partial decryptions
> partial_decryptions = [get_partial_decryption(encrypted_message, share) for share in threshold_keys.sk_arr]
> #Decrypt message
> decrypted_message = elgamal_dec_threshold(partial_decryptions, encrypted_message, ThresholdParameters(number_of_tellers, number_of_tellers))
> print(decrypted_message)
Encr this mess
"""


def threshold(k, n):
    """
    generates (k, n) threshold system (k secret keys out of n needed to decrypt the message)
    returns ThresholdKeys object storing pkT (election public key and n key shares (sk_i))
    """
    thresh_params = ThresholdParameters(k, n)
    pub_key, key_shares = ThresholdCrypto.create_public_key_and_shares_centralized(parameters, thresh_params)
    PK = El(type_G, pub_key.g_a)
    key_shares = [El(type_Z, key_shares[i].y, i + 1) for i in range(len(key_shares))]
    threshold_keys = ThresholdKeys(PK, key_shares)

    return threshold_keys


def get_partial_decryption(cipher, sk_i):
    """
    A partial decryption (x_i, v^(y_i)) of a ciphertext computed by a share owner using his share.
    returns PartialDecryption object.
    """
    p = sk_i.parameters.p
    v_y = gmpy2.powmod(cipher.v, sk_i.value, p)
    partial_decryption = PartialDecryption(sk_i.id, v_y)

    return partial_decryption

def combine_shares(partial_decryptions,
                    cipher,
                    threshold_params):

        # compute lagrange coefficients
        partial_indices = [dec.id for dec in partial_decryptions]
        lagrange_coefficients = number.build_lagrange_coefficients(partial_indices, parameters.q)

        factors = [
            gmpy2.powmod(partial_decryptions[i].v_y, lagrange_coefficients[i], parameters.p)
            for i in range(0, len(partial_decryptions))
        ]
        restored_g_ka = number.prod(factors) % parameters.p
        restored_g_minus_ak = number.prime_mod_inv(restored_g_ka, parameters.p)
        restored_m = cipher.c * restored_g_minus_ak % parameters.p

        return restored_m

def elgamal_enc_threshold(pk, message):
    encrypted = ThresholdCrypto.encrypt_message(pk, message)
    cipher = ThresholdCipher(encrypted.v, encrypted.c, encrypted.enc)

    return cipher

def elgamal_dec_threshold(partial_decryptions,
                            cipher,
                            threshold_params):
        """
        Decrypt a message using the combination of at least t partial decryptions. Similar to the encryption process
        the hybrid approach is used for decryption.

        partial_decryptions: at least t partial decryptions
        cipher: the encrapted message to be decrypted
        threshold_params: the used threshold parameters
        
        returns the decrypted message
        """
        key_subgroup_element = int(combine_shares(
            partial_decryptions,
            cipher,
            threshold_params
        ))
        # print('HERE:', type(int(key_subgroup_element)))
        key_subgroup_element_byte_length = (key_subgroup_element.bit_length() + 7) // 8
        key_subgroup_element_bytes = key_subgroup_element.to_bytes(key_subgroup_element_byte_length, byteorder='big')

        try:
            key = nacl.hash.blake2b(key_subgroup_element_bytes,
                                    digest_size=nacl.secret.SecretBox.KEY_SIZE,
                                    encoder=nacl.encoding.RawEncoder)
            box = nacl.secret.SecretBox(key)
            encoded_plaintext = box.decrypt(bytes.fromhex(cipher.enc))
        except nacl.exceptions.CryptoError as e:
            raise ThresholdCryptoError('Message decryption failed. Internal: ' + str(e))

        return str(encoded_plaintext, 'utf-8')

