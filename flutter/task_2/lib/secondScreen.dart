import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SecondScreen extends StatefulWidget {
  const SecondScreen({super.key});


  @override
  State<StatefulWidget> createState() {
    return _SecondScreenState();
  }
}

class _SecondScreenState extends State<SecondScreen> {
  String inputValue = '';


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CupertinoButton(
              child: const Text("Go Back"),
              onPressed: () {
                Navigator.pop(context, inputValue);
              },
            ),
            Container(
              width: 300,
              height: 50,
              child: TextField(onChanged: (value){
                inputValue = value;
              }),
            )
          ],
        ),
      ),
    );
  }
}
