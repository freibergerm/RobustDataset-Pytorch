import torch

class IORobustDataset(torch.utils.data.Dataset):

    def __getattribute__(self, name):

        super_attr = super().__getattribute__(name)
        if callable(super_attr):
            #TODO: Check whether it pays off in terms of performance to use a LUT here?
            def run_guarded_function(*args,**kwargs):
                i = 0
                while True:
                    try:
                        return super_attr(*args,**kwargs)
                    except (FileNotFoundError, AttributeError, OSError, PermissionError) as e:
                        print(e)
                        sleep_time = 0.1 * 10 ** i
                        print(f'Exponential retry: sleep for {sleep_time} seconds before retrying')
                        time.sleep(sleep_time)
                        i += 1

            return run_guarded_function
        else:
            return super_attr

