#OLD TEST
enqueue_job_call = list(nsq_mock.method_calls[0])



#NEW TEST THAT TESTS ALREADY CREATED CODE
nsq_mock.assert_not_called()

#SHOULD HAVE BEEN
nsq_mock.enqueue_job.assert_not_called()