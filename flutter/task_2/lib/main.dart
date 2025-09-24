import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Flutter Demo', home: MyHomePage());
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({super.key});

  @override
  State<StatefulWidget> createState() {
    return _State();
  }
}

class _State extends State<MyHomePage> {
  var currentColor = 0;
  var colors = [Colors.orange, Colors.blueAccent, Colors.green, Colors.amber];
  var displayText = [];

  void _onNumberPressed(int number) {
    setState(() {
      displayText.add(number.toString());
    });
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              alignment: Alignment.center,
              color: colors[currentColor],
              width: 300,
              height: 200,
            ),
            SizedBox(height: 20),
            CupertinoButton(
              child: Text('Change Color'),
              onPressed: () {
                setState(() {
                  if (currentColor >= colors.length - 1) {
                    currentColor = 0;
                    return;
                  }
                  currentColor += 1;
                });
              },
            ),
            SizedBox(height: 30),
            Text(displayText.toString()),
            SizedBox(height: 20),
            Column(
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(onPressed: () => _onNumberPressed(1), child: Text('1')),
                    SizedBox(width: 10),
                    ElevatedButton(onPressed: () => _onNumberPressed(2), child: Text('2')),
                    SizedBox(width: 10),
                    ElevatedButton(onPressed: () => _onNumberPressed(3), child: Text('3')),
                  ],
                ),
                SizedBox(height: 10),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(onPressed: () => _onNumberPressed(4), child: Text('4')),
                    SizedBox(width: 10),
                    ElevatedButton(onPressed: () => _onNumberPressed(5), child: Text('5')),
                    SizedBox(width: 10),
                    ElevatedButton(onPressed: () => _onNumberPressed(6), child: Text('6')),
                  ],
                ),
                SizedBox(height: 10),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(onPressed: () => _onNumberPressed(7), child: Text('7')),
                    SizedBox(width: 10),
                    ElevatedButton(onPressed: () => _onNumberPressed(8), child: Text('8')),
                    SizedBox(width: 10),
                    ElevatedButton(onPressed: () => _onNumberPressed(9), child: Text('9')),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}