late = [time.strptime(t, '%H:%M:%S') > time.strptime('14:40:00', '%H:%M:%S')
        for t in submission_times]