import torch
from torchvision.transforms import transforms
from torchvision import models
import torch.nn as nn

def get_model(num_classes):
    model = models.resnet18()
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, num_classes)
    return model

def load_model(model_path, num_classes_default=144):
    checkpoint = torch.load(model_path)
    num_classes = checkpoint.get('num_classes', num_classes_default)
    model = get_model(num_classes=num_classes)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    return model

def predict_image(binaryImg, model, transform):
    image = transform(binaryImg).unsqueeze(0) 
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    return predicted.item()

def predict(image):
    model_path = 'model.pth'
    class_labels = ['1355868', '1355932', '1355936', '1355937', '1355978', '1355990', '1356022', '1356075', '1356111', '1356126', '1356257', '1356382', '1356420', '1356421', '1356428', '1356692', '1356781', '1357330', '1357635', '1357677', '1358094', '1358095', '1358105', '1358133', '1358150', '1358605', '1358689', '1358751', '1358752', '1358766', '1359197', '1359483', '1359485', '1359488', '1359498', '1359517', '1359525', '1359616', '1359620', '1359625', '1359669', '1360153', '1360588', '1360590', '1360671', '1360811', '1360978', '1360998', '1361024', '1361656', '1361666', '1361759', '1361823', '1361824', '1362294', '1362490', '1362954', '1363021', '1363110', '1363128', '1363129', '1363130', '1363227', '1363336', '1363490', '1363699', '1363737', '1363740', '1363749', '1363764', '1363991', '1364099', '1364159', '1364164', '1364172', '1364173', '1367432', '1369887', '1369960', '1374048', '1384485', '1385937', '1389510', '1390637', '1391192', '1391226', '1391483', '1391652', '1391797', '1391953', '1392475', '1392695', '1392777', '1393241', '1393393', '1393414', '1393423', '1393425', '1393449', '1393466', '1393614', '1393725', '1393792', '1393946', '1394120', '1394382', '1394399', '1394404', '1394420', '1394454', '1394460', '1394489', '1394504', '1394591', '1394994', '1396708', '1396824', '1397268', '1397303', '1397312', '1397364', '1397420', '1398128', '1398178', '1398444', '1398515', '1398592', '1399145', '1399783', '1400100', '1402921', '1408774', '1408961', '1409238', '1409292', '1409295', '1418146', '1418547', '1420795', 
'1420863', '1421021', '1435714', '1529081', '1529328']

    model = load_model(model_path)

    data_transforms = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    predicted_class = predict_image(image, model, data_transforms)

    return class_labels[predicted_class]
