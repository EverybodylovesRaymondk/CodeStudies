	�g��s�@�g��s�@!�g��s�@	���xf�?���xf�?!���xf�?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$�g��s�@F���Ը@A��_vO�?Y�����B�?*	33333Cf@2F
Iterator::Model��~j�t�?!Ȗ�VE@)�ʡE��?1�d�*al@@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate��ݓ���?!�d�=@)�ܵ�|У?1�����5@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat	�^)ˠ?!�Q���j2@)�?�߾�?1O��N��.@:Preprocessing2U
Iterator::Model::ParallelMapV2�Q���?!��ī�#@)�Q���?1��ī�#@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip����9#�?!8ij�L@)�ZӼ��?1����f�@:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice��<,Ԋ?!���k@)��<,Ԋ?1���k@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor��_vOv?!��.��A@)��_vOv?1��.��A@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMapK�46�?!����>@)F%u�k?1���q��?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
both�Your program is POTENTIALLY input-bound because 78.4% of the total step time sampled is spent on 'All Others' time (which could be due to I/O or Python execution or both).no*no9���xf�?>Look at Section 3 for the breakdown of input time on the host.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	F���Ը@F���Ը@!F���Ը@      ��!       "      ��!       *      ��!       2	��_vO�?��_vO�?!��_vO�?:      ��!       B      ��!       J	�����B�?�����B�?!�����B�?R      ��!       Z	�����B�?�����B�?!�����B�?JCPU_ONLYY���xf�?b 