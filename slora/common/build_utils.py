
def repair_config(config, same_names):
    find_value = next(
        (
            config[name]
            for name in same_names
            if name in config and config[name] is not None
        ),
        None,
    )
    for name in same_names:
        config[name] = find_value
    return