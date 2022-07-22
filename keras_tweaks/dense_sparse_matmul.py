import tensorflow as tf


def dense_sparse_matmul(denV: tf.Tensor, spW: tf.SparseTensor) -> tf.Tensor:
    """Multiply row vector with sparse matrix

    Parameters:
        denV (tf.Tensor): Dense BxN or BxTxN dense tensor.
        spW (tf.SparseTensor): Sparse NxM matrix.

    Returns:
        tf.Tensor: Dense BxM or BxTxM dense tensor

    Motivation:
        TF only supports multiplying a sparse matrix with a column vector.
        By transposing, we can use `tf.sparse.sparse_dense_matmul` to
        multiply a row vector with a sparse matrix. The later multiplication
        is commonly used in context of neural networks in TF/Keras.
    """
    # reshape to list of row vectors if neccessary
    if denV.shape.ndims == 1:
        denV = tf.reshape(denV, (1, -1))

    # transpose -> multiply -> transpose back
    if denV.shape.ndims == 2:
        # W * V_(batch, dim)
        return tf.transpose(tf.sparse.sparse_dense_matmul(
            tf.sparse.transpose(spW, perm=[1, 0]),
            tf.transpose(denV, perm=[1, 0])))

    if denV.shape.ndims == 3:
        # W * V_(batch, seqlen, dim)
        Wt = tf.sparse.transpose(spW, perm=[1, 0])
        ht = tf.transpose(denV, perm=[0, 2, 1])
        out = []
        for ex in ht:
            out.append(tf.sparse.sparse_dense_matmul(Wt, ex))
        return tf.transpose(tf.stack(out), perm=[0, 2, 1])

    raise ValueError("Invalid shape: {}".format(denV.shape))
