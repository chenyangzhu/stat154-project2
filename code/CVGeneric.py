def CVGeneric(classifier, img_train, K, loss_func, cvsplit_method, **kwargs):
  # Input:
    # Classifier:     function    a classifier object
    # img:            dataframe   training features
    # K:              int         K-fold CV
    # loss_func:      function    a loss function
  # Output:
    # K-fold CV loss  float       loss

  cv_label = cvsplit_method(img_train, K)

  val_acc = []
  loss = []
  
  # Change img_train indexing for logistic models
  img = img_train.copy()
  img['label'] = np.where(img['label'] == -1.0, 0.0,1.0)
  start = time.time()
  for k in range(K):
    # CV Training data

    img_cvval = img.loc[cv_label[k]]
    img_cvtrain = img.drop(cv_label[k])

    # Use the remaining cv_label to test
    predictions = classifier(img_cvtrain, img_cvval, **kwargs)
    val_acc.append(np.mean(predictions == img_cvval['label']))
    loss.append(loss_func(predictions, img_cvval['label']))
  print("--- %s seconds ---" % (time.time() - start))
  outcome = {}
  outcome['val_acc'] = val_acc
  outcome['loss'] = loss
  
  return outcome
